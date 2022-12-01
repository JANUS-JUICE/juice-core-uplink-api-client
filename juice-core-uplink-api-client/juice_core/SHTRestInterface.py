import json
import logging
from typing import List, Union
from functools import cache
import pandas as pd
from attr import define

log = logging.getLogger(__name__)

from juice_core_uplink_api_client.api.rest_api import (
    rest_api_events_list,
    rest_api_plan_list,
    rest_api_plan_read,
    rest_api_series_list,
    rest_api_trajectory_engineering_segments_list,
    rest_api_trajectory_event_list,
    rest_api_trajectory_series_list,
)
from juice_core_uplink_api_client.client import Client


def convert_times(table, columns=None):
    if isinstance(columns, str):
        columns = [columns]

    if columns is not None:
        for c in columns:
            table[c] = pd.to_datetime(table[c]).dt.tz_localize(None)

    return table


DEFAULT_START = "2020"
DEFAULT_END = "2040"

from functools import partial
from merge_args import merge_args


def pandas_convertable(func=None, timefields=None):
    if func is None:
        return partial(pandas_convertable, timefields=timefields)

    @merge_args(func)
    def wrapper(*args, as_pandas=True, **kwargs ):


        result = func(*args, **kwargs)
        if as_pandas:
            return convert_times(pd.DataFrame([d.to_dict() for d in result]),
                          columns=timefields)
        else:
            return result


    return wrapper



@define(auto_attribs=True, eq=False )
class SHTRestInterface:
    """
    Main entry point for interacting with the Juice Core Uplink API
    """

    client: [None, Client] = None
    timeout: float = 40.0

    def __attrs_post_init__(self):
        if not self.client:
            self.client = Client("https://juicesoc.esac.esa.int")
        self.client.timeout = self.timeout

    @cache
    @pandas_convertable(timefields=["created"])
    def plans(self):
        """Retrieve all the plans available on the endpoint"""
        return rest_api_plan_list.sync(client=self.client)

    def plan_id_by_name(self, name):
        """Retrieve the plan id from the plane name"""
        for plan in self.plans():
            if plan.name.lower().strip() == name.lower().strip():
                log.debug(f"Plan {name} has id {plan.id}")
                return plan.id

        log.warning(f"No plan with name {name} found")
        return None

    @cache
    @pandas_convertable(timefields=["start", "end"])
    def plan_segments(self, plan_id_or_name):
        """Retrieve the segments of a plan"""
        plan = self.plan(plan_id_or_name, as_pandas=False)
        return plan.segments

    @cache
    @pandas_convertable(timefields=["start", "end"])
    def engineering_segments(self, trajectory="CREMA_5_0") -> pd.DataFrame:
        """Retrieve the engineering segments for a mnemonic"""
        return rest_api_trajectory_engineering_segments_list.sync(mnemonic=trajectory, client=self.client)

    @cache
    @pandas_convertable
    def plan(self, plan_id_or_name):
        """Retrieve the plan from the plan id or name"""
        if isinstance(plan_id_or_name, str):
            plan_id_or_name = self.plan_id_by_name(plan_id_or_name)
        return rest_api_plan_read.sync(plan_id_or_name, client=self.client)

    @cache
    @pandas_convertable
    def known_series(self, trajectory="CREMA_5_0"):
        """Retrieve all the series available on the endpoint"""
        return rest_api_trajectory_series_list.sync(client=self.client, mnemonic=trajectory)

    @cache
    @pandas_convertable(timefields=["epoch"])
    def series(self, series_name, trajectory="CREMA_5_0", start=DEFAULT_START, end=DEFAULT_END):
        """Retrieve a serie from the endpoint"""

        q = dict(start=str(start), end=str(end), trajectory=trajectory, series=series_name)

        body = json.dumps(q)
        return rest_api_series_list.sync(client=self.client, body=body)

    @cache
    @pandas_convertable(timefields=None)
    def event_types(self, trajectory="CREMA_5_0"):
        """Retrieve all the events applicable for a trajectory"""
        return rest_api_trajectory_event_list.sync(client=self.client, mnemonic=trajectory)

    @cache
    @pandas_convertable(timefields=["start", "end"])
    def events(
        self,
        mnemonics: Union[List[str], str] = [],
        trajectory:str="CREMA_5_0",
        start=DEFAULT_START,
        end=DEFAULT_END,
    ):
        """Retrieve events of a given type from the endpoint"""
        
        from time import sleep
        sleep(5)
        if isinstance(mnemonics, str):
            mnemonics = [mnemonics]

        if len(mnemonics) == 0:
            mnemonics = self.event_types(trajectory=trajectory, as_pandas=False)
            mnemonics = [m.name for m in mnemonics]
            log.info(f"Retrieving all known events {mnemonics}")

        q = dict(start=str(start), end=str(end), trajectory=trajectory, mnemonics=mnemonics)

        body = json.dumps(q)
        return rest_api_events_list.sync(client=self.client, body=body)



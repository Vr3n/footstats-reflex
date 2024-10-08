import reflex as rx
from typing import Dict, List

from footstats_reflex.supabase_client import get_supabase_client


class CompetitionState(rx.State):
    competitions: List[Dict[str, str]] = []

    def all_competitions(self) -> List[Dict[str, str]]:
        session = get_supabase_client()
        res = session.table('competition').select('name',
                                                  'logo').execute()
        print(res)
        self.competitions = res.data

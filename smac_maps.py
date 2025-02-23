from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pysc2.maps import lib


class SMACMap(lib.Map):
    directory = "SMAC_Maps"
    download = "https://github.com/oxwhirl/smac#smac-maps"
    players = 2
    step_mul = 8
    game_steps_per_episode = 0


map_param_registry = {
    "10sp_zerg": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 3,
        "map_type": "zerg_gen",
        "map_name": "32x32_flatsp",
    },
    "10sp_protoss": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "protoss_gen",
        "map_name": "32x32_flatsp",
    },
    "10sp_terran": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "terran_gen",
        "map_name": "32x32_flatsp",
    },
    "10gen_terran": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "terran_gen",
        "map_name": "32x32_flat",
    },
    "10gen_zerg": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 3,
        "map_type": "zerg_gen",
        "map_name": "32x32_flat",
    },
    "10gen_protoss": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 200,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "protoss_gen",
        "map_name": "32x32_flat",
    },
    "3m": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 60,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "3m",
    },
    "8m": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "8m",
    },
    "25m": {
        "n_agents": 25,
        "n_enemies": 25,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "25m",
    },
    "5m_vs_6m": {
        "n_agents": 5,
        "n_enemies": 6,
        "limit": 70,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "5m_vs_6m",
    },
    "8m_vs_9m": {
        "n_agents": 8,
        "n_enemies": 9,
        "limit": 120,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "8m_vs_9m",
    },
    "10m_vs_11m": {
        "n_agents": 10,
        "n_enemies": 11,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "10m_vs_11m",
    },
    "27m_vs_30m": {
        "n_agents": 27,
        "n_enemies": 30,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "27m_vs_30m",
    },
    "MMM": {
        "n_agents": 10,
        "n_enemies": 10,
        "limit": 150,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "MMM",
        "map_name": "MMM",
    },
    "MMM2": {
        "n_agents": 10,
        "n_enemies": 12,
        "limit": 180,
        "a_race": "T",
        "b_race": "T",
        "unit_type_bits": 3,
        "map_type": "MMM",
        "map_name": "MMM2",
    },
    "2s3z": {
        "n_agents": 5,
        "n_enemies": 5,
        "limit": 120,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
        "map_name": "2s3z",
    },
    "3s5z": {
        "n_agents": 8,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
        "map_name": "3s5z",
    },
    "3s5z_vs_3s6z": {
        "n_agents": 8,
        "n_enemies": 9,
        "limit": 170,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 2,
        "map_type": "stalkers_and_zealots",
        "map_name": "3s5z_vs_3s6z",
    },
    "3s_vs_3z": {
        "n_agents": 3,
        "n_enemies": 3,
        "limit": 150,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
        "map_name": "3s_vs_3z",
    },
    "3s_vs_4z": {
        "n_agents": 3,
        "n_enemies": 4,
        "limit": 200,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
        "map_name": "3s_vs_4z",
    },
    "3s_vs_5z": {
        "n_agents": 3,
        "n_enemies": 5,
        "limit": 250,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "stalkers",
        "map_name": "3s_vs_5z",
    },
    "1c3s5z": {
        "n_agents": 9,
        "n_enemies": 9,
        "limit": 180,
        "a_race": "P",
        "b_race": "P",
        "unit_type_bits": 3,
        "map_type": "colossi_stalkers_zealots",
        "map_name": "1c3s5z",
    },
    "2m_vs_1z": {
        "n_agents": 2,
        "n_enemies": 1,
        "limit": 150,
        "a_race": "T",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "marines",
        "map_name": "2m_vs_1z",
    },
    "corridor": {
        "n_agents": 6,
        "n_enemies": 24,
        "limit": 400,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "zealots",
        "map_name": "corridor",
    },
    "6h_vs_8z": {
        "n_agents": 6,
        "n_enemies": 8,
        "limit": 150,
        "a_race": "Z",
        "b_race": "P",
        "unit_type_bits": 0,
        "map_type": "hydralisks",
        "map_name": "6h_vs_8z",
    },
    "2s_vs_1sc": {
        "n_agents": 2,
        "n_enemies": 1,
        "limit": 300,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "stalkers",
        "map_name": "2s_vs_1sc",
    },
    "so_many_baneling": {
        "n_agents": 7,
        "n_enemies": 32,
        "limit": 100,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "zealots",
        "map_name": "so_many_baneling",
    },
    "bane_vs_bane": {
        "n_agents": 24,
        "n_enemies": 24,
        "limit": 200,
        "a_race": "Z",
        "b_race": "Z",
        "unit_type_bits": 2,
        "map_type": "bane",
        "map_name": "bane_vs_bane",
    },
    "2c_vs_64zg": {
        "n_agents": 2,
        "n_enemies": 64,
        "limit": 400,
        "a_race": "P",
        "b_race": "Z",
        "unit_type_bits": 0,
        "map_type": "colossus",
        "map_name": "2c_vs_64zg",
    },
}


def get_smac_map_registry():
    return map_param_registry


for name, map_params in map_param_registry.items():
    globals()[name] = type(
        name, (SMACMap,), dict(filename=map_params["map_name"])
    )

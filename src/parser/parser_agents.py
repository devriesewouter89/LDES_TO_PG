from src.utils.utils import *
import json


def generate_dataframe_AGENTS(config):
    df_agents = pd.DataFrame(generate_dataframe("AGENT", config))

    for i in range(0, len(config.columns_agents)):
        df_agents.insert(i, config.columns_agents[i], "")

    for i in range(0, len(df_agents)):
        x = df_agents.loc[i]
        j = json.loads(x[0])

        uri, type = j["@id"], j["@type"]
        df_agents.at[i, "URI"] = uri
        df_agents.at[i, "@type"] = type

        fetch_timestamp(df_agents, i, j)
        fetch_agent_fullname(df_agents, i, j)
        fetch_agent_family_name(df_agents, i, j)
        fetch_agent_first_name(df_agents, i, j)
        fetch_agent_same_as(df_agents, i, j)
        fetch_agent_birthdate(df_agents, i, j)
        fetch_agent_birthplace(df_agents, i, j)
        fetch_agent_deathplace(df_agents, i, j)
        fetch_agent_date_of_death(df_agents, i, j)

    return df_agents


if __name__ == "__main__":
    generate_dataframe_AGENTS()

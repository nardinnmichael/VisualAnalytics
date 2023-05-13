import ijson
import pandas as pd
import time
import networkit as nk
import os


def parse_tweets_as_df(filename):
    start = time.time()
    columns_to_keep = ["ID", "tweet", "profile.id", "profile.name", "profile.followers_count", "profile.friends_count",
                       "profile.verified", "profile.statuses_count", "neighbor.following", "neighbor.follower"]
    with open(filename, 'r') as file:
        objects = ijson.items(file, 'item')

        dfs = []  # create an empty list to store DataFrames

        for obj in objects:
            obj_df = pd.json_normalize(obj)
            try:
                obj_df = obj_df[columns_to_keep]
                dfs.append(obj_df)
            except:
                ()
        df = pd.concat(dfs, ignore_index=True)
        df['ID'] = df['ID'].astype(int)
        df['profile.id'] = df['profile.id'].astype(int)
        df['profile.followers_count'] = df['profile.followers_count'].astype(int)
        df['profile.friends_count'] = df['profile.friends_count'].astype(int)
        df['profile.verified'] = df['profile.verified'].astype(bool)
        df['profile.statuses_count'] = df['profile.statuses_count'].astype(int)

        end = time.time()

        print(f"Parsed {df['ID'].count()} users in",  "{:.2f}".format(end - start), " seconds.")
        return df

def get_graph(df, directed=True):
    # Create a directed graph
    G = nk.Graph(directed=directed)

    # Create dictionaries for mapping
    id_to_node = {}
    node_to_id = {}

    # Add nodes and edges to the graph
    for idx, row in df.iterrows():
        user_id = row['ID']

        # If the user_id is not in the dictionary, add a new node
        if user_id not in id_to_node:
            new_node = G.addNode()
            id_to_node[user_id] = new_node
            node_to_id[new_node] = user_id

        for following_id in row['neighbor.following']:
            # If the following_id is not in the dictionary, add a new node
            if following_id not in id_to_node:
                new_node = G.addNode()
                id_to_node[following_id] = new_node
                node_to_id[new_node] = following_id

            G.addEdge(id_to_node[user_id], id_to_node[following_id])

        for follower_id in row['neighbor.follower']:
            # If the follower_id is not in the dictionary, add a new node
            if follower_id not in id_to_node:
                new_node = G.addNode()
                id_to_node[follower_id] = new_node
                node_to_id[new_node] = follower_id

            G.addEdge(id_to_node[follower_id], id_to_node[user_id])
    # print(nk.overview(G))
    print(f"There are {G.numberOfEdges()} edges")
    # write the graph to file

    if not os.path.isdir('./output/'):
        os.makedirs('./output')
    nk.writeGraph(G, "./output/twitter_usersSNAP", nk.Format.SNAP)

    # TODO: if we get this to work, we wouldn't have to parse and filter the graphs from the twitter data
    # end of function
    # K = nk.readGraph("./output/twitter_users", nk.Format.SNAP)
    # K = nk.graphio.SNAPGraphReader().read("./output/twitter_usersSNAP")
    # for n1, n2, attr in G.edges(data=True):
    #     print(n1, n2, attr)
    if directed is True:
        G_x = nk.nxadapter.nk2nx(G)  # convert from NetworKit.Graph to networkx.Graph
        return G, G_x
    else:
        return G, None

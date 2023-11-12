from util import environment_classes

# call the waterworld_ppo class with custom options -- only one agent needs to touch, and only one pursuer
single_agent = environment_classes.waterworld_ppo(log_dir='log_dir/single_agent_preset_env', n_coop = 1, n_pursuers = 1)

# we're going to run a train/test loop. 20 iterations of each, 100,000 steps per training loop, 10 games per evaluation set
single_agent.interlace_run(num_loops=3, num_games=3, num_steps=1000)

# now let's plot the results
single_agent.plot_rewards()
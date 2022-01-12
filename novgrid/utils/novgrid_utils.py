import gym_minigrid
import gym


def make_env(env_name, log_dir, wrappers=[]):
    '''
    I think that you have to have this function because the 
    vectorization code expects a function wrappers is a list
    '''
    def _init():
        env = gym.make(env_name)
        if wrappers:
            for wrapper in wrappers:
                env = wrapper(env)
        return env
    return _init


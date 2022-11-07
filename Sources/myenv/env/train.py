import gym
from rl.agents.dqn import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.policy import EpsGreedyQPolicy
from rl.memory import SequentialMemory
from rl.processors import MultiInputProcessor
from CardGameEnv import CardGameEnv
from tensorflow import keras
from keras.optimizers import Adam
from keras.layers import Dense, Activation, Flatten, Input, concatenate
from keras.models import Sequential,Model
from keras.utils import plot_model
import numpy as np
import sys

from rl.callbacks import (
    TrainEpisodeLogger,
    TrainIntervalLogger,
    FileLogger
)


# 環境の生成
env = CardGameEnv()
action_history = []
reward_history = []
nb_actions = env.action_space.n
#print(nb_actions)
print(env.observation_space)
#observation_value_list = list(env.observation_space.values())
#bservation_arr = np.empty(1,len(observation_value_list))
#for i in observation_value_list:
#    observation_arr.append(i)
#print(observation_arr)

"""
環境デバック用テストコード(CPUでも動く)
for _ in range(200):
    action = env.action_space.sample()
    action_history.append(action)
    print("action.history: ")
    print(action_history)
    obs, re, done, info = env.step(action)
    reward_history.append(re)
    if done:
        action_history = []
        env.reset()
print(reward_history)
"""




# モデルの定義(ここ雰囲気で書いてる)
model_MyHP = Sequential()
model_MyHP.add(Flatten(input_shape=(1,1), name='MyHP'))
model_MyHP_input = Input(shape=(1,1), name='MyHP')
model_MyHP_encoded = model_MyHP(model_MyHP_input)

model_EnemyHP = Sequential()
model_EnemyHP.add(Flatten(input_shape=(1,1), name='EnemyHP'))
model_EnemyHP_input = Input(shape=(1,1), name='EnemyHP')
model_EnemyHP_encoded = model_EnemyHP(model_EnemyHP_input)

model_MyCard1Attack = Sequential()
model_MyCard1Attack.add(Flatten(input_shape=(1,1), name='MyCard1Attack'))
model_MyCard1Attack_input = Input(shape=(1,1), name='MyCard1Attack')
model_MyCard1Attack_encoded = model_MyCard1Attack(model_MyCard1Attack_input)

model_MyCard1HP = Sequential() 
model_MyCard1HP.add(Flatten(input_shape=(1,1), name='MyCard1HP'))
model_MyCard1HP_input = Input(shape=(1,1), name='MyCard1HP')
model_MyCard1HP_encoded = model_MyCard1HP(model_MyCard1HP_input)

model_MyCard2Attack = Sequential()
model_MyCard2Attack.add(Flatten(input_shape=(1,1), name='MyCard2Attack'))
model_MyCard2Attack_input = Input(shape=(1,1), name='MyCard2Attack')
model_MyCard2Attack_encoded = model_MyCard2Attack(model_MyCard2Attack_input)

model_MyCard2HP = Sequential() 
model_MyCard2HP.add(Flatten(input_shape=(1,1), name='MyCard2HP'))
model_MyCard2HP_input = Input(shape=(1,1), name='MyCard2HP')
model_MyCard2HP_encoded = model_MyCard2HP(model_MyCard2HP_input)

model_MyCard3Attack = Sequential()
model_MyCard3Attack.add(Flatten(input_shape=(1,1), name='MyCard3Attack'))
model_MyCard3Attack_input = Input(shape=(1,1), name='MyCard3Attack')
model_MyCard3Attack_encoded = model_MyCard3Attack(model_MyCard3Attack_input)

model_MyCard3HP = Sequential() 
model_MyCard3HP.add(Flatten(input_shape=(1,1), name='MyCard3HP'))
model_MyCard3HP_input = Input(shape=(1,1), name='MyCard3HP')
model_MyCard3HP_encoded = model_MyCard3HP(model_MyCard3HP_input)

model_EnemyCard1Attack = Sequential()
model_EnemyCard1Attack.add(Flatten(input_shape=(1,1), name='EnemyCard1Attack'))
model_EnemyCard1Attack_input = Input(shape=(1,1), name='EnemyCard1Attack')
model_EnemyCard1Attack_encoded = model_EnemyCard1Attack(model_EnemyCard1Attack_input)

model_EnemyCard1HP = Sequential() 
model_EnemyCard1HP.add(Flatten(input_shape=(1,1), name='EnemyCard1HP'))
model_EnemyCard1HP_input = Input(shape=(1,1), name='EnemyCard1HP')
model_EnemyCard1HP_encoded = model_EnemyCard1HP(model_EnemyCard1HP_input)

model_EnemyCard2Attack = Sequential()
model_EnemyCard2Attack.add(Flatten(input_shape=(1,1), name='EnemyCard2Attack'))
model_EnemyCard2Attack_input = Input(shape=(1,1), name='EnemyCard2Attack')
model_EnemyCard2Attack_encoded = model_EnemyCard2Attack(model_EnemyCard2Attack_input)

model_EnemyCard2HP = Sequential() 
model_EnemyCard2HP.add(Flatten(input_shape=(1,1), name='EnemyCard2HP'))
model_EnemyCard2HP_input = Input(shape=(1,1), name='EnemyCard2HP')
model_EnemyCard2HP_encoded = model_EnemyCard2HP(model_EnemyCard2HP_input)

model_EnemyCard3Attack = Sequential()
model_EnemyCard3Attack.add(Flatten(input_shape=(1,1), name='EnemyCard3Attack'))
model_EnemyCard3Attack_input = Input(shape=(1,1), name='EnemyCard3Attack')
model_EnemyCard3Attack_encoded = model_EnemyCard3Attack(model_EnemyCard3Attack_input)

model_EnemyCard3HP = Sequential() 
model_EnemyCard3HP.add(Flatten(input_shape=(1,1), name='EnemyCard3HP'))
model_EnemyCard3HP_input = Input(shape=(1,1), name='EnemyCard3HP')
model_EnemyCard3HP_encoded = model_EnemyCard3HP(model_EnemyCard3HP_input)

model_MyCard1CanAttack = Sequential() 
model_MyCard1CanAttack.add(Flatten(input_shape=(1,1), name='MyCard1CanAttack'))
model_MyCard1CanAttack_input = Input(shape=(1,1), name='MyCard1CanAttack')
model_MyCard1CanAttack_encoded = model_MyCard1CanAttack(model_MyCard1CanAttack_input)

model_MyCard2CanAttack = Sequential() 
model_MyCard2CanAttack.add(Flatten(input_shape=(1,1), name='MyCard2CanAttack'))
model_MyCard2CanAttack_input = Input(shape=(1,1), name='MyCard2CanAttack')
model_MyCard2CanAttack_encoded = model_MyCard2CanAttack(model_MyCard2CanAttack_input)

model_MyCard3CanAttack = Sequential() 
model_MyCard3CanAttack.add(Flatten(input_shape=(1,1), name='MyCard3CanAttack'))
model_MyCard3CanAttack_input = Input(shape=(1,1), name='MyCard3CanAttack')
model_MyCard3CanAttack_encoded = model_MyCard3CanAttack(model_MyCard3CanAttack_input)

con = concatenate([model_MyHP_encoded, 
                    model_EnemyHP_encoded, 
                    model_MyCard1Attack_encoded,
                    model_MyCard1HP_encoded, 
                    model_MyCard2Attack_encoded, 
                    model_MyCard2HP_encoded,
                    model_MyCard3Attack_encoded, 
                    model_MyCard3HP_encoded, 
                    model_EnemyCard1Attack_encoded, 
                    model_EnemyCard1HP_encoded,
                    model_EnemyCard2Attack_encoded,
                    model_EnemyCard2HP_encoded,
                    model_EnemyCard3Attack_encoded,
                    model_EnemyCard3HP_encoded,
                    model_MyCard1CanAttack_encoded,
                    model_MyCard2CanAttack_encoded,
                    model_MyCard3CanAttack_encoded
                ])

hidden = Dense(16, activation='relu')(con)
for _ in range(2): 
	hidden = Dense(16, activation='relu')(hidden)
output = Dense(nb_actions, activation='linear')(hidden)
model_final = Model(inputs=[
                            model_MyHP_input, 
                            model_EnemyHP_input, 
                            model_MyCard1Attack_input, 
                            model_MyCard1HP_input,
                            model_MyCard2Attack_input,
                            model_MyCard2HP_input,
                            model_MyCard3Attack_input,
                            model_MyCard3HP_input,
                            model_EnemyCard1Attack_input,
                            model_EnemyCard1HP_input,
                            model_EnemyCard2Attack_input,
                            model_EnemyCard2HP_input,
                            model_EnemyCard3Attack_input,
                            model_EnemyCard3HP_input,
                            model_MyCard1CanAttack_input,
                            model_MyCard2CanAttack_input,
                            model_MyCard3CanAttack_input
                        ],
                    outputs=output)
#print(model_final.summary())
plot_model(model_final, to_file='model.png')

# エージェントの設定
memory = SequentialMemory(limit=50000, window_length=1)
policy = BoltzmannQPolicy()
dqn = DQNAgent(model=model_final, nb_actions=nb_actions, memory=memory, nb_steps_warmup=2000,
               target_model_update=1e-2, policy=policy)
dqn.processor = MultiInputProcessor(17)
dqn.compile(Adam(learning_rate=1e-3), metrics=['mae'])

#学習
dqn.fit(env, nb_steps=int(1e5), visualize=False, verbose=1, callbacks=[ TrainEpisodeLogger()])

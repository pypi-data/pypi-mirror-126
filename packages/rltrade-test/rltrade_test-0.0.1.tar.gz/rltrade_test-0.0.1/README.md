# rl-trade

## Python 3.7.11 or greater is required

# pyfolio pip version has bugs so run this
    git clone https://github.com/quantopian/pyfolio.git
    cd pyfolio
    pip install -e .

# You can now pip install the library for testing.
    pip install -i https://test.pypi.org/simple/ rltrade-test==0.0.34

### Import and setup
```python
import os
from rltrade import config
from rltrade.models import DRLAgent
from rltrade.environments import StockTradingEnv
from rltrade.data import FeatureEngineer,YahooDownloader,time_seires_split

os.makedirs("./testdata/" + config.DATA_SAVE_DIR,exist_ok=True)
os.makedirs("./testdata/" + config.TRAINED_MODEL_DIR,exist_ok=True)
os.makedirs("./testdata/" + config.TENSORBOARD_LOG_DIR,exist_ok=True)
os.makedirs("./testdata/" + config.RESULTS_DIR,exist_ok=True)

```

### Downloading data and setting up environment
```python
ticker = config.FAANG_TICKER_DICT['apple']

print('Downloading Data')
df = YahooDownloader(start_date = '2009-01-01',
                        end_date = '2021-01-01',
                        ticker_list = ticker).fetch_data()

print("Preprocessing data")
df = FeatureEngineer(stock_indicators=True,
                    stock_indicator_list=config.STOCK_INDICATORS_LIST).create_data(df)

train = time_seires_split(df, start = '2009-01-01', end = '2019-01-01')
trade = time_seires_split(df, start = '2019-01-01', end = '2021-01-01')

stock_dimension = len(train['tic'].unique())
state_space = 1 + 2*stock_dimension + len(config.STOCK_INDICATORS_LIST)*stock_dimension
print(f"Stock data Dimensions: {stock_dimension}, State Spaces: {state_space}")
env_kwargs = {
    "hmax": 100, 
    "initial_amount": 100000, 
    "buy_cost_pct": 0.001, 
    "sell_cost_pct":0.001,
    "state_space": state_space, 
    "stock_dim": stock_dimension, 
    "tech_indicator_list": config.STOCK_INDICATORS_LIST, 
    "action_space": stock_dimension, 
    "reward_scaling": 1e-4}
e_train_gym = StockTradingEnv(df=train,**env_kwargs)
env_train, _ = e_train_gym.get_sb_env()

e_trade_gym = StockTradingEnv(df=trade,**env_kwargs)
env_trade,obs_trade = e_trade_gym.get_sb_env()

```
### Training model and trading

```python
def test_trade():
    agent = DRLAgent(env = env_train)
    PPO_PARAMS = {'n_steps':2048,
                'ent_coef':0.005,
                'learning_rate':0.0001,
                'batch_size':128}

    model_ppo = agent.get_model("ppo",model_kwargs=PPO_PARAMS)
    print("PPO train start")
    trained_ppo = agent.train_model(model=model_ppo,
                                    tb_log_name='ppo',
                                    total_timesteps=5000)
    print("Training PPO success")

    df_account_value,df_actions = DRLAgent.DRL_prediction(model=trained_ppo,
                                                            environment=e_trade_gym)
    print("Trading Success")

    print("BackTesting")
    perf_stats_all = backtest_stats(account_value=df_account_value)
    perf_stats_all = pd.DataFrame(perf_stats_all)

    backtest_plot(account_value=df_account_value,
                baseline_ticker='AAPL',
                baseline_start = '2019-01-01', 
                baseline_end = '2021-01-01')
    print("BackTesting Sucess")

if __name__ == "__main__":
    test_trade()

```

# Note
    copy the code from FinRL github do not use finrl library.
    write all the test cases in test.py
    if your test cases or example contains any data output store it in testdata folder.
    
# Plan for this library
    FinRL library uses very deprecated libraries and functions so we will build our own
    library based on FinRL.

    The structure and flow of our library will be similar to the FinRL but implementation
    will be ours.

    This is the flow of our library and our project.
    1. YahooDownloader to get the data.
    2. We have to recreate FeatureEngineering library.
    3. We have to integrate new data splitting techniques.
    4. We have to build our own environment using OpenAI and help of FinRL library.
    5. Then we will recreate models and training code for this library.

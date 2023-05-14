# declaration of library
import tensorflow as tf
from keras.utils import Sequence
from keras.models import Sequential
from keras.layers import SimpleRNN
from keras.layers import LSTM
from keras.layers import GRU
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import TimeDistributed
from keras.layers import Bidirectional
from keras.optimizers import Adam, Adamax, RMSprop, SGD

# define class model
class model:

    # method model stacked bidirectional lstm
    def stacked_bidirectional_lstm(x_train, y_train, x_test, y_test):
        
        # fix random seed generator
        tf.random.set_seed(1234);

        # The LSTM-RNN architecture
        model = tf.keras.Sequential([
            
            # First LSTM layer with Dropout regularisation
            tf.keras.layers.Bidirectional(
                LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1))
            ),
            
            # Secound LSTM layer with Dropout regularisation
            tf.keras.layers.Bidirectional(
                LSTM(units=50, return_sequences=False)
            ),
            
            # The output layer
            tf.keras.layers.Dense(1)
        ]);

        # Compile the model LSTM
        model.compile(optimizer='adam', loss='mean_squared_error')

        # fit network
        history = model.fit(x_train, y_train, batch_size=8, epochs=50, validation_data=(x_test, y_test), verbose=1, use_multiprocessing=True, shuffle=False)

        # return values
        return model, history;

      
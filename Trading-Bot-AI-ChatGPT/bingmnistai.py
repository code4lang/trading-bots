# Importar TensorFlow y otros módulos necesarios
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# Cargar el dataset MNIST desde TensorFlow Datasets
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalizar los valores de los píxeles entre 0 y 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Crear un modelo secuencial con tres capas: una capa de entrada plana, una capa oculta densa con 128 neuronas y función de activación ReLU, y una capa de salida densa con 10 neuronas y función de activación softmax
model = keras.Sequential([
  keras.layers.Flatten(input_shape=(28, 28)),
  keras.layers.Dense(128, activation='relu'),
  keras.layers.Dense(10, activation='softmax')
])

# Compilar el modelo con el optimizador Adam, la función de pérdida entropía cruzada categórica y la métrica precisión
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entrenar el modelo con los datos de entrenamiento durante 10 épocas
model.fit(x_train, y_train, epochs=10)

# Evaluar el modelo con los datos de prueba y mostrar el resultado
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('\nTest loss:', test_loss)
print('Test accuracy:', test_acc)

# Mostrar algunas predicciones del modelo con los datos de prueba y sus etiquetas reales
predictions = model.predict(x_test)
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_test[i], cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    true_label = y_test[i]
    if predicted_label == true_label:
      color = 'blue'
    else:
      color = 'red'
    plt.xlabel("{} ({})".format(predicted_label,
                                  true_label),
                                  color=color)
plt.show()
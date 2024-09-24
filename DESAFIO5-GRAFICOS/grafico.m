% Definir la matriz A y el vector b
A = [1.0001, 1.0000; 
     1.0000, 1.0000];
b = [2; 2];

% Resolver el sistema de ecuaciones A * x = b
x = A \ b;

% Crear la gráfica
x_vals = linspace(-10, 10, 200);

% Ecuación de la primera fila de A * x = b: 1.0001*x + 1*y = 2
y1_vals = (2 - 1.0001 * x_vals) / 1.0;

% Ecuación de la segunda fila de A * x = b: 1*x + 1*y = 2
y2_vals = (2 - 1.0 * x_vals) / 1.0;

% Graficar las líneas
plot(x_vals, y1_vals, 'b', 'DisplayName', '1.0001x + y = 2');
hold on;
plot(x_vals, y2_vals, 'r--', 'DisplayName', 'x + y = 2');

% Graficar la solución
plot(x(1), x(2), 'ro', 'MarkerSize', 8, 'DisplayName', sprintf('Solución (%.4f, %.4f)', x(1), x(2)));

% Añadir etiquetas y leyenda
xlabel('x');
ylabel('y');
title('Gráfica del sistema de ecuaciones');
legend('show');
grid on;

hold off;

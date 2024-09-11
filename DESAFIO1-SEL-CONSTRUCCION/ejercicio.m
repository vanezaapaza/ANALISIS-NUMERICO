% Definir la matriz de coeficientes
Matriz = [0.52, 0.20, 0.25;
          0.30, 0.50, 0.20;
          0.18, 0.30, 0.55];
% Definir el vector de resultados
resultado = [4800; 5210; 5690];
% Resolver el sistema de ecuaciones
solucion = Matriz \ resultado;

% Mostrar la solución
disp('Las cantidades de metros cúbicos que se deben extraer desde cada cantera son:');
disp(['Cantera A: ', num2str(solucion(1)), ' metros cúbicos']);
disp(['Cantera B: ', num2str(solucion(2)), ' metros cúbicos']);
disp(['Cantera C: ', num2str(solucion(3)), ' metros cúbicos']);
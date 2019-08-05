eps = 0.05;
last = eps;
cut = 1;
true_eps = last;
iterations = 0;
while iterations < 100
    iterations = iterations + 1;
    while 1 ~= eps + 1
        last = eps;
        eps = eps / (1 + cut);
        if 1+cut == 1
            break
        end
    end
    eps = last;
    cut = cut / 2;
end

fprintf('Machine epsilon: %g\n',last)

max_number = 1;
true_max_number = 0;
iterations = 0;

while max_number < Inf
    true_max_number = max_number;
    max_number = max_number * 2;
    iterations = iterations + 1;
end

iterations = iterations - 1;

max_number = 0;
true_max_number = 0;
while iterations > 0
    true_max_number = max_number;
    max_number = max_number + 2^iterations;
    if max_number == Inf
        break;
    end
    iterations = iterations - 1;
end

fprintf("Machine biggest positive integer: %g", true_max_number)

"""
Scientific computation, finding roots of functions.
"""


line = function(x)
    return (3 * x - 2)
end


function bisect(fn, a, b, err)
    x = a + (b - a) / 2
    y = fn(x)
    i = 1
    while abs(y) > err
        if y * fn(a) > 0
            a = x
        else
            b = x
        end
        x = a + (b - a) / 2
        y = fn(x)
        i += 1
    end
    return (x, i)
end


function regula_falsi(fn, a, b, err)
    x = (a * fn(b) - b * fn(a))/(fn(b) - fn(a))
    y = fn(x)
    i = 1
    while abs(y) > err
        if y * fn(a) > 0
            a = x
        else
            b = x
        end
        x = (a * fn(b) - b * fn(a))/(fn(b) - fn(a))
        y = fn(x)
        i += 1
    end
    return (x, i)
end


function secant_method(fn, a, b, err)
    x = b - fn(b)*(a - b) / (fn(a) - fn(b))
    i = 1
    while abs(fn(x)) > err
        b = a
        a = x
        x = b - fn(b)*(a - b) / (fn(a) - fn(b))
        println(x)
        i += 1
    end
    return (x, i)
end

println("Methods with total number of iterations")
println("Bisection")
println(bisect(line, -10, 10, 0.001))
println(bisect(line, -20, 30, 0.001))
println(bisect(line, -1, 10, 0.001))

println("Regula falsi")
println(regula_falsi(line, -10, 10, 0.001))
println(regula_falsi(line, -20, 30, 0.001))
println(regula_falsi(line, -1, 10, 0.001))

println("Secant method")
println(secant_method(line, -10, 10, 0.001))
println(secant_method(line, -20, 30, 0.001))
println(secant_method(line, -1, 10, 0.001))

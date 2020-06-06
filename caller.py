from julia import Main as jl
jl.include("mylib.jl")


if __name__ == '__main__':
    res = jl.add(1, 1)
    print(res)
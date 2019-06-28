# Global variable & Local variable

g_variable = None


def fun():
    global g_variable
    g_variable = 20
    return g_variable + 100


print("g_variable past:", g_variable)
fun()
print("g_variable now", g_variable)

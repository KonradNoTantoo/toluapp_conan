#include <cstdlib>
#include <iostream>

extern "C"
{
#include "lua.h"
}

#include "tolua++.h"

int main()
{
    lua_State *L = lua_open();

    if (NULL == L) {
        std::cerr << "Error Initializing lua" << std::endl;
        return EXIT_FAILURE;
    }

    tolua_open(L);
    lua_close(L);
    return EXIT_SUCCESS;
}

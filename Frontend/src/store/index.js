import { createStore } from "vuex";
import ModuleUser from "./user";
import ModuleNet from "./net";
export default createStore({
    state: {

    },
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        user: ModuleUser,
        net: ModuleNet,
    },
});
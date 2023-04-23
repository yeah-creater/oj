import $ from "jquery";
// import jwt_decode from "jwt-decode";
const ModuleUser = {
    state: {
        ip: 'https://app2105.acapp.acwing.com.cn',
        id: 0,
        name: "",
        sno: "",
        gender: '',
        birthday: '',
        photo: '',
        record: '',
        access: "",
        refresh: "",
        notification_count: 0,
        is_login: false,
        socket: '',
    },
    getters: {},

    // 不能执行异步操作, 同步进行
    mutations: {
        updateUser(state, user) {
            state.name = user.name;
            state.sno = user.sno;
            state.id = user.id;
            state.gender = user.gender;
            state.birthday = user.birthday;
            state.photo = user.photo;
            state.record = user.record;
            state.access = user.access;
            state.refresh = user.refresh;
            state.is_login = user.is_login;
            state.notification_count = user.notification_count;
            localStorage.setItem('access', user.access);
            localStorage.setItem('refresh', user.refresh);
            state.socket = new WebSocket('wss://app2105.acapp.acwing.com.cn/wss/chat/list/?token=' + state.access);
        },
        updateAccess(state, access) {
            state.access = access;
            localStorage.setItem('access', access);
        },
        logout(state) {
            state.name = "";
            state.sno = "";
            state.id = 0;
            state.gender = '';
            state.birthday = '';
            state.photo = "";
            state.record = "";
            state.access = "";
            state.refresh = "";
            state.is_login = false;
            state.notification_count = 0;
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            state.socket.close();
            state.socket = '';
        },

    },
    actions: {
        getInfo(context) {
            const access = localStorage.getItem('access');
            const refresh = localStorage.getItem('refresh');
            if (!access || !refresh) return;
            // const access_obj = jwt_decode(access);
            setInterval(() => {
                $.ajax({
                    url: context.state.ip + "/api/token/refresh/",
                    type: "POST",
                    data: {
                        refresh,
                    },
                    success(res) {
                        context.commit("updateAccess", res.access);
                    },
                });
            }, 4.5 * 60 * 1000);
            if (!access) return;
            $.ajax({
                url: context.state.ip + "/settings/getinfo/",
                type: "GET",
                async: false,
                headers: {
                    Authorization: "Bearer " + access,
                },
                success(res) {
                    if (res.result === 'success') {
                        res = res.data;
                        context.commit("updateUser", {
                            ...res,
                            access: access,
                            refresh: refresh,
                            is_login: true,
                        });
                    } else {
                        alert(res.result)
                    }
                },
            });
        },
        logout(context) {
            $.ajax({
                url: context.state.ip + "/settings/logout/",
                type: "POST",
                headers: {
                    Authorization: "Bearer " + localStorage.getItem('access'),
                },
                success(res) {
                    if (res.result === 'success') {
                        context.commit("logout")
                    } else {
                        alert(res.result)
                    }

                },
            });
        },
        login(context, data) {
            $.ajax({
                url: context.state.ip + "/api/token/",
                type: "POST",
                data: {
                    username: data.username,
                    password: data.password,
                    code: data.code,
                    uuid: data.uuid,
                },
                success(res) {
                    if (res.result == 'fail') {
                        data.error();
                        return;
                    }
                    const { access, refresh } = res;
                    setInterval(() => {
                        if (!refresh) return;
                        $.ajax({
                            url: context.state.ip + "/api/token/refresh/",
                            type: "POST",
                            data: {
                                refresh,
                            },
                            success(res) {
                                context.commit("updateAccess", res.access);
                            },
                        });
                    }, 4.5 * 60 * 1000);
                    $.ajax({
                        url: context.state.ip + "/settings/getinfo/",
                        type: "GET",
                        async: false,
                        headers: {
                            Authorization: "Bearer " + access,
                        },
                        success(res) {
                            if (res.result === 'success') {
                                res = res.data;
                                context.commit("updateUser", {
                                    ...res,
                                    access: access,
                                    refresh: refresh,
                                    is_login: true,
                                });
                                data.success();
                            } else {
                                alert(res.result)
                            }

                        },
                    });
                },
                error() {
                    data.error();
                },
            });
        },

    },
    modules: {},
};
export default ModuleUser;
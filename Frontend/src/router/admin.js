import AdminView from '@/views/admin/AdminView';
import AdminProblemView from "@/views/admin/problem/AdminProblemView";
import AdminProblemAddView from "@/views/admin/problem/add/AdminProblemAddView";
import AdminVideoView from '@/views/admin/video/AdminVideoView';
import AdminVideoAddView from "@/views/admin/video/add/AdminVideoAddView";
import AdminContestView from '@/views/admin/contest/AdminContestView';
import AdminContestAddView from "@/views/admin/contest/add/AdminContestAddView";
const admin = [{
        path: '/auth/admin/',
        name: 'admin',
        component: AdminView,
    }, {
        path: '/auth/admin/problem/',
        name: 'admin_problem',
        component: AdminProblemView,
    },
    {
        path: '/auth/admin/problem/add/',
        name: 'admin_problem_add',
        component: AdminProblemAddView,
    },
    {
        path: '/auth/admin/video/',
        name: 'admin_video',
        component: AdminVideoView,
    },
    {
        path: '/auth/admin/video/add/',
        name: 'admin_video_add',
        component: AdminVideoAddView,
    },
    {
        path: '/auth/admin/contest/',
        name: 'admin_contest',
        component: AdminContestView,
    },
    {
        path: '/auth/admin/contest/add/',
        name: 'admin_contest_add',
        component: AdminContestAddView,
    },
]


export default admin
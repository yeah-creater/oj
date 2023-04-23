import { createRouter, createWebHashHistory } from 'vue-router'
import $ from "jquery";
// import jwt_decode from "jwt-decode";
import admin from './admin'
import HomeView from '@/views/HomeView.vue';
import ContestView from '@/views/contest/ContestView.vue';
import ContestRatingView from '@/views/contest/rating/ContestRatingView.vue';
import ContestContentView from '@/views/contest/content/ContestContentView.vue';
import ContestContentProblemView from '@/views/contest/content/problem/ContestContentProblemView.vue';
import ContestContentStandingView from '@/views/contest/content/standing/ContestContentStandingView.vue';
import ContestContentDiscussionView from '@/views/contest/content/discussion/ContestContentDiscussionView.vue';

import VideoContentView from '@/views/video/content/VideoContentView'
import AppView from '@/views/app/AppView.vue';
import AppChatView from '@/views/app/chat/AppChatView.vue';
import AppCalculationView from '@/views/app/calculation/AppCalculationView.vue';
import AppKofView from '@/views/app/kof/AppKofView.vue';
import AppPlayerView from '@/views/app/player/AppPlayerView.vue';
import SolutionView from '@/views/solution/SolutionView.vue';
import SolutionContentView from '@/views/solution/content/SolutionContentView.vue'
import SolutionAddView from '@/views/solution/add/SolutionAddView.vue'
import SolutionUpdateView from '@/views/solution/update/SolutionUpdateView.vue'
import SolutionSearchView from '@/views/solution/search/SolutionSearchView.vue'
import BlogView from '@/views/blog/BlogView.vue';
import BlogSearchView from '@/views/blog/search/BlogSearchView.vue';
import BlogAddView from '@/views/blog/add/BlogAddView.vue';
import BlogContentView from '@/views/blog/content/BlogContentView.vue';
import BlogUpdateView from '@/views/blog/update/BlogUpdateView.vue';
import LoginView from '@/views/LoginView.vue';
import RegisterView from '@/views/RegisterView.vue';
import MyspaceView from '@/views/user/MyspaceView.vue';
import MyspaceFollowView from '@/views/user/myspace/MyspaceFollowView.vue';
import MyspaceRecordView from '@/views/user/myspace/MyspaceRecordView.vue';
import MyspaceSolutionView from '@/views/user/myspace/MyspaceSolutionView.vue';
import MyspaceBlogView from '@/views/user/myspace/MyspaceBlogView.vue';
import MyspaceNotificationView from '@/views/user/myspace/MyspaceNotificationView.vue';
import SettingView from '@/views/user/Setting.vue';
import SettingAccountView from '@/views/user/setting/SettingAccountView.vue'
import NotFoundView from '@/views/NotFoundView.vue';
import ProblemContentView from '@/views/problem/content/ProblemContentView.vue';
import ProblemDashboardView from '@/views/problem/dashboard/ProblemDashboardView.vue';
import ProblemDashboardSearchView from '@/views/problem/dashboard/search/ProblemDashboardSearchView.vue';
import ProblemMineView from '@/views/problem/mine/ProblemMineView.vue';
import SubmitRecordView from '@/views/submit_record/SubmitRecordView';
let routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/problem/',
        name: 'problem',
        redirect: ("/problem/dashboard/1/"),
    },
    {
        path: '/submit_record/:submission_id/',
        name: 'submit_record',
        component: SubmitRecordView,
    },
    {
        path: '/problem/dashboard/:id/',
        name: 'problem_dashboard',
        component: ProblemDashboardView,
    },
    {
        path: '/problem/dashboard/search/:search/:page/',
        name: 'problem_dashboard_search',
        component: ProblemDashboardSearchView,
    },
    {
        path: '/problem/mine/',
        name: 'problem_mine',
        component: ProblemMineView,
    },

    {
        path: '/problem/content/:id/',
        component: ProblemContentView,
        name: 'problem_content',
    },
    {
        path: '/video/content/:id',
        name: 'video_content',
        component: VideoContentView
    },
    {
        path: '/contest/rating/',
        name: 'contest_rating',
        component: ContestRatingView
    },
    {
        path: '/contest/:id/',
        name: 'contest',
        component: ContestView
    },
    {
        path: '/contest/content/:id/',
        name: 'contest_content',
        component: ContestContentView,
        children: [{
                path: 'problem/',
                component: ContestContentProblemView,
                name: 'contest_content_problem',
            },
            {
                path: 'standing/',
                component: ContestContentStandingView,
                name: 'contest_content_standing',
            },
            {
                path: 'discussion/',
                component: ContestContentDiscussionView,
                name: 'contest_content_discussion',
            },
        ]
    },
    {
        path: '/app/',
        name: 'app',
        component: AppView
    },
    {
        path: '/app/chat/',
        name: 'app_chat',
        component: AppChatView
    },
    {
        path: '/app/calculation/',
        name: 'app_calculation',
        component: AppCalculationView
    },
    {
        path: '/app/kof/',
        name: 'app_kof',
        component: AppKofView
    },
    {
        path: '/app/player/',
        name: 'app_player',
        component: AppPlayerView
    },
    {
        path: '/solution/:id/',
        name: 'solution',
        component: SolutionView
    },
    {
        path: '/solution/search/:search/:page/',
        name: 'solution_search',
        component: SolutionSearchView
    },
    {
        path: '/solution/content/:id/',
        name: 'solution_content',
        component: SolutionContentView
    },
    {
        path: '/solution/add/',
        name: 'solution_add',
        component: SolutionAddView
    },
    {
        path: '/solution/update/:id/',
        name: 'solution_update',
        component: SolutionUpdateView
    },

    {
        path: '/blog/:id/',
        name: 'blog',
        component: BlogView
    },
    {
        path: '/blog/add/',
        name: 'blog_add',
        component: BlogAddView
    },
    {
        path: '/blog/content/:id/',
        name: 'blog_content',
        component: BlogContentView
    },
    {
        path: '/blog/search/:search/:page/',
        name: 'blog_search',
        component: BlogSearchView
    },
    {
        path: '/blog/update/:id/',
        name: 'blog_update',
        component: BlogUpdateView
    },
    {
        path: '/auth/login/',
        name: 'login',
        component: LoginView
    },
    {
        path: '/auth/register/',
        name: 'register',
        component: RegisterView
    },

    {
        path: '/user/myspace/:userId/',
        name: 'user_myspace',
        component: MyspaceView,
        children: [{
                path: 'record/',
                component: MyspaceRecordView,
                name: 'user_mysapce_record',
            },
            {
                path: 'solution/',
                component: MyspaceSolutionView,
                name: 'user_mysapce_solution',
            },
            {
                path: 'blog/',
                component: MyspaceBlogView,
                name: 'user_mysapce_blog',
            }, {
                path: 'follower/',
                component: MyspaceFollowView,
                name: 'user_mysapce_follower',
            }, {
                path: 'following/',
                component: MyspaceFollowView,
                name: 'user_mysapce_following',
            },
            {
                path: 'notification/',
                component: MyspaceNotificationView,
                name: 'user_mysapce_notification',
            }
        ],
    },
    {
        path: '/user/setting/',
        name: 'user_setting',
        component: SettingView,
    },
    {
        path: '/user/setting/account/',
        name: 'user_setting_account',
        component: SettingAccountView,
    },

    {
        path: '/404/',
        name: '404',
        component: NotFoundView
    },
    {
        path: '/:catchAll(.*)',
        redirect: "/404/"
    },

]
routes = routes.concat(admin)
const router = createRouter({
    history: createWebHashHistory(),
    routes,
})
router.beforeEach((to) => {
    if (to.path.startsWith("/auth/admin/")) {
        const access = localStorage.getItem('access');
        const refresh = localStorage.getItem('refresh');
        if (!access || !refresh) {
            router.push({ name: '404' });
            return;
        }
        // const access_obj = jwt_decode(access);
        $.ajax({
            url: "https://app2105.acapp.acwing.com.cn/settings/getinfo/",
            type: "GET",
            async: false,
            headers: {
                Authorization: "Bearer " + access,
            },
            success(res) {
                if (res.result === 'success') {
                    res = res.data;
                    if (res.id !== 1) router.push({ name: '404' });
                    return;
                }
            },
            error() {
                router.push({ name: '404' });
                return;
            }
        });
    }
});

export default router
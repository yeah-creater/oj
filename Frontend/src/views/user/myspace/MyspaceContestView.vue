<template>
    <ContentBaseSecondary >
        <div style="height:500px" ref="categoryChart"></div>
    </ContentBaseSecondary>
</template>

<script>
//调用echarts
import * as echarts from 'echarts';
import ContentBaseSecondary from '@/components/ContentBaseSecondary.vue';
export default {
    components: {ContentBaseSecondary},
    name: "MyspaceContestView",
    data() {
        return {
        };
    },
    methods: {
        find() {
            this.chart = echarts.init(this.$refs.categoryChart);
            const option = {
                title: {
                    text: '积分等级金字塔',
                },
                // tooltip: {
                //     trigger: 'item',
                //     formatter: "{a} <br/>{b} : {c}%"
                // },
                // toolbox: {
                //     feature: {
                //         dataView: { readOnly: false },
                //         restore: {},
                //         saveAsImage: {}
                //     }
                // },
                // legend: {
                //     data: ['灰色', '点击', '访问', '咨询', '订单', '灰色', '点击', '访问', '咨询', '订单']
                // },

                series: [
                    {
                        sort:'ascending',
                        name: '漏斗图',
                        type: 'funnel',
                        left: '10%',
                        top: 60,
                        bottom: 60,
                        width: '80%',
                        min: 0,
                        max: 100,
                        minSize: '0%',
                        maxSize: '100%',
                        gap: 3,
                        label: {
                            show: true,
                            position: 'outside'
                        },
                        labelLine: {
                            length: 10,
                            lineStyle: {
                                width: 1,
                                type: 'solid'
                            }
                        },
                        itemStyle: {
                            borderColor: "#fff",
                            borderWidth: 1,
                            normal: {
                                color: function (params) {
                                    //自定义颜色
                                    var colorList = [
                                        "#AA0000",
                                        "#AA0000",
                                        "#FF3333",
                                        "#FF3333",
                                        "#FF7777",
                                        "#FF7777",
                                        "#FFBB55",
                                        "#FFBB55",
                                        "#FFCC88",
                                        "#FFCC88",
                                        "#FF88FF",
                                        "#FF88FF",
                                        "#AAAAFF",
                                        "#AAAAFF",
                                        "#77DDBB",
                                        "#77DDBB",
                                        "#77FF77",
                                        "#77FF77",
                                        "#CCCCCC",
                                        "#CCCCCC",
                                    ];
                                    return colorList[params.dataIndex];
                                }
                            }
                        },
                        emphasis: {
                            label: {
                                fontSize: 18
                            }
                        },
                        data: [
                            { value: 10, name: 'Legendary Grandmaster' },
                            { value: 10, name: '[3000,+∞)' },
                            { value: 20, name: 'International Grandmaster' },
                            { value: 20, name: '[2600,3000)' },
                            { value: 30, name: 'Grandmaster' },
                            { value: 30, name: '[2400,2600)' },
                            { value: 40, name: 'International Master' },
                            { value: 40, name: '[2300,2400)' },
                            { value: 50, name: 'Master' },
                            { value: 50, name: '[2100,2300)' },
                            { value: 60, name: 'Candidate Master' },
                            { value: 60, name: '[1900,2100)' },
                            { value: 70, name: 'Expert' },
                            { value: 70, name: '[1600,1900)' },
                            { value: 80, name: 'Specialist' },
                            { value: 80, name: '[1400,1600)' },
                            { value: 90, name: 'Pupil' },
                            { value: 90, name: '[1200,1400)' },
                            { value: 100, name: 'Newbier' },
                            { value: 100, name: '(0,1200)' },
                        ]
                    }
                ]
            };
            this.chart.setOption(option);
        }
    },
    mounted() {
        this.find();
    },
    created() { }
};
</script>

<style  lang="less" scoped></style>
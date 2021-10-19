import {mount, createLocalVue, shallowMount} from '@vue/test-utils';
import server from '../utils/server-api';
import AxiosMockAdapter from 'axios-mock-adapter';
import flushPromises from "flush-promises";

import Result from '../views/Result';
import Vuetify from "vuetify";

const chartData = {
    "start_point": -0.5,
    "end_point": 1.5,
    "iterations": [
        {
            "start_point": 0,
            "end_point": 49,
            "start_point_value": -0.5,
            "end_point_value": 1.5,
            "y_value": 0.2639,
            "f_y_value": 0.0697,
            "z_value": 0.7361,
            "f_z_value": 0.5418,
            "is_left_slice": true,
            "is_right_slice": false,
            "iteration": 0
        },
        {
            "start_point": 0,
            "end_point": 30.2837,
            "start_point_value": -0.5,
            "end_point_value": 0.7361,
            "y_value": -0.0279,
            "f_y_value": 0.0008,
            "z_value": 0.2639,
            "f_z_value": 0.0697,
            "is_left_slice": true,
            "is_right_slice": false,
            "iteration": 1
        },
        {
            "start_point": 0,
            "end_point": 18.7163,
            "start_point_value": -0.5,
            "end_point_value": 0.2639,
            "y_value": -0.2082,
            "f_y_value": 0.0433,
            "z_value": -0.0279,
            "f_z_value": 0.0008,
            "is_left_slice": false,
            "is_right_slice": true,
            "iteration": 2
        },
        {
            "start_point": 7.149,
            "end_point": 18.7163,
            "start_point_value": -0.2082,
            "end_point_value": 0.2639,
            "y_value": -0.0279,
            "f_y_value": 0.0008,
            "z_value": 0.0836,
            "f_z_value": 0.007,
            "is_left_slice": true,
            "is_right_slice": false,
            "iteration": 3
        },
        {
            "start_point": 7.149,
            "end_point": 14.298,
            "start_point_value": -0.2082,
            "end_point_value": 0.0836,
            "y_value": -0.0967,
            "f_y_value": 0.0094,
            "z_value": -0.0279,
            "f_z_value": 0.0008,
            "is_left_slice": false,
            "is_right_slice": true,
            "iteration": 4
        },
        {
            "start_point": 9.8797,
            "end_point": 14.298,
            "start_point_value": -0.0967,
            "end_point_value": 0.0836,
            "y_value": -0.0279,
            "f_y_value": 0.0008,
            "z_value": 0.0147,
            "f_z_value": 0.0002,
            "is_left_slice": false,
            "is_right_slice": true,
            "iteration": 5
        },
        {
            "start_point": 11.5673,
            "end_point": 14.298,
            "start_point_value": -0.0279,
            "end_point_value": 0.0836,
            "y_value": 0.0147,
            "f_y_value": 0.0002,
            "z_value": 0.041,
            "f_z_value": 0.0017,
            "is_left_slice": true,
            "is_right_slice": false,
            "iteration": 6
        }
    ],
    "number_of_iterations": 7,
    "result": 0.0066,
    "formula": "$x^{2}$",
    "x_values": [
        -0.5,
        -0.4592,
        -0.4184,
        -0.3776,
        -0.3367,
        -0.2959,
        -0.2551,
        -0.2143,
        -0.1735,
        -0.1327,
        -0.0918,
        -0.051,
        -0.0102,
        0.0306,
        0.0714,
        0.1122,
        0.1531,
        0.1939,
        0.2347,
        0.2755,
        0.3163,
        0.3571,
        0.398,
        0.4388,
        0.4796,
        0.5204,
        0.5612,
        0.602,
        0.6429,
        0.6837,
        0.7245,
        0.7653,
        0.8061,
        0.8469,
        0.8878,
        0.9286,
        0.9694,
        1.0102,
        1.051,
        1.0918,
        1.1327,
        1.1735,
        1.2143,
        1.2551,
        1.2959,
        1.3367,
        1.3776,
        1.4184,
        1.4592,
        1.5
    ],
    "y_values": [
        0.25,
        0.2109,
        0.1751,
        0.1426,
        0.1134,
        0.0876,
        0.0651,
        0.0459,
        0.0301,
        0.0176,
        0.0084,
        0.0026,
        0.0001,
        0.0009,
        0.0051,
        0.0126,
        0.0234,
        0.0376,
        0.0551,
        0.0759,
        0.1,
        0.1275,
        0.1584,
        0.1925,
        0.23,
        0.2708,
        0.3149,
        0.3624,
        0.4133,
        0.4674,
        0.5249,
        0.5857,
        0.6498,
        0.7172,
        0.7882,
        0.8623,
        0.9397,
        1.0205,
        1.1046,
        1.192,
        1.283,
        1.3771,
        1.4745,
        1.5753,
        1.6794,
        1.7868,
        1.8978,
        2.0119,
        2.1293,
        2.25
    ],
    "number_of_points": 50,
    "acc": 0.1
}

const chartId = 0;

describe('Result component tests', () => {
    const localVue = createLocalVue()
    let vuetify
    let axios

    beforeEach(() => {
        vuetify = new Vuetify()

        axios = new AxiosMockAdapter(server);

        axios.onGet(/\/graphic\/\d+/).reply(200, chartData);
    })

    test('Check result data in component', async () => {
        // mount() returns a wrapped Vue component we can interact with
        const wrapper = mount(Result, { localVue, vuetify, propsData: { id: chartId } });

        await flushPromises();

        expect(wrapper.find('[data-test=result]').text()).toEqual(chartData['result'].toString());
        expect(wrapper.find('[data-test=pointA]').text()).toEqual(chartData['start_point'].toString());
        expect(wrapper.find('[data-test=pointB]').text()).toEqual(chartData['end_point'].toString());
        expect(wrapper.find('[data-test=eps]').text()).toEqual(chartData['acc'].toString());
        expect(wrapper.find('[data-test=numberOfIterations]').text()).toEqual(chartData['number_of_iterations'].toString());
        expect(wrapper.find('[data-test=currentIter]').text()).toEqual('1');
    });


    test('Must redirect when chart with given id is not exists', async () => {
        const invalidChartId = -1;
        const mockRouter = {
            push: jest.fn()
        };


        const wrapper = mount(Result, {
            localVue,
            vuetify,
            propsData: { id: invalidChartId },
            mocks: {
                $router: mockRouter,
            }
        });

        axios.onGet(/\/graphic\/\d+/).replyOnce(400, {});

        await flushPromises();

        expect(mockRouter.push).toHaveBeenCalledTimes(1)
        expect(mockRouter.push).toHaveBeenCalledWith({name: 'Home'})
    });

    test('Match chart snapshot', async () => {
        const wrapper = shallowMount(Result, { localVue, vuetify, propsData: { id: chartId } });

        await wrapper.vm.$nextTick();

        expect(wrapper.find('canvas').element).toMatchSnapshot();
    })
});
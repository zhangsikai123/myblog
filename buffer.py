#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : sikai.zhang
# @Time    : 11/5/19 2:38 PM


class DimensionOrderBuffer(object):

    def __init__(self):
        # if not RedEnv.is_dev():  # 本地开发为了加快速度
        # for d in EvaluationQuestion.get_by_query({}).order_by('id'):
        #     aid = d.activity_id
        #     aggregation = EvaluationActivityAggregation.get_by_id(aid)
        #     if not aggregation:
        #         continue
        #     ecid = aggregation.evaluation_category_id
        #     if ecid not in _dimension_order:
        #         _dimension_order[ecid] = {}
        #     if d.index_name not in _dimension_order[ecid]:
        #         _dimension_order[ecid][d.index_name] = len(
        #             _dimension_order[ecid].keys())

        _dimension_order = {'test': 'haha'}
        self._buffer = _dimension_order

    def get(self, evaluation_category_id, dimension_name):
        return self._buffer.get(evaluation_category_id, {}).get(dimension_name, float('inf'))


dimension_order = DimensionOrderBuffer()

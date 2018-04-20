#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : pureoym
# @Contact : pureoym@163.com
# @TIME    : 2018/4/20 9:17
# @File    : test.py
# Copyright 2017 pureoym. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    train_path = 'D:/data/preliminary_contest_data/adFeature.csv'
    df = pd.DataFrame(pd.read_csv(train_path))

    # aid  advertiserId  campaignId creativeId  creativeSize
    # adCategoryId productId  productType
    # print df.info()

    # 按照advertiserId排序，查看advertiserId对应creativeId个数
    df = df.sort_values(by=['advertiserId'])
    # print df.groupby('aid').count() # 173
    # print df.groupby('advertiserId').count() # 79
    # print df.groupby('campaignId').count() #138
    # print df.groupby('creativeId').count() #173
    print df.describe()





if __name__ == '__main__':
    main()

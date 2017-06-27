#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 生成200个优惠码
# 此处设定优惠码为8位随机数字或大写字母。
# ASCII编码48-57代表数字0-9；编码65-90代表大写字母A-Z

import random

def rand_char():
    # 优惠码备选字符放入一个list
    rand_list = list(range(48,58)) + list(range(65,91))
    # 从list随机选择一个index
    n = random.randint(0, len(rand_list) - 1)
    return chr(rand_list[n])

def generate_coupon():
    coupon = ''
    while len(coupon) < 8:
        coupon += rand_char()
    return coupon

def generate_coupon_list(n):
    count = 0
    coupons = []

    while count < n:
        random_coupon = generate_coupon()
        # 检查是否有重复的coupon
        if random_coupon not in coupons:
            coupons.append(random_coupon)
            count += 1

    return coupons

print (generate_coupon_list(10))

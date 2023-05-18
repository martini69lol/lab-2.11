#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def zamik():
    f = input('Фамилия: ')
    n = input('Имя: ')

    def make_shab(f, n):
        shab = f'Уважаемый {f}, {n}! Вы делаете работу по замыканиям функций'
        return shab

    result = make_shab(f, n)
    print(result)


if __name__ == "__main__":
    zamik()

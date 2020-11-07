class SuperSeriosTest:
    def test(self):
        run = True
        while run:
            question = input('ты лох? ')
            if question == 'да':
                print('Я обязательно это сохраню))))0))0)0)')
                run = False
            elif question == 'нет':
                print('пидора ответ. Ты пидор :)')
                run = False
            else:
                print('ok')

        for i in range(100):
            # print('Марья Ивановна, я реально больше не буду!')
            pass


if __name__ == '__main__':
    SuperSeriosTest().test()




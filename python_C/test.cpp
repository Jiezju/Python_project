#include <stdio.h>
#include <malloc.h>

//�޲������޷�������
extern "C" void hello()
{
    printf("Hello,NEU!\n");
}

//�в������з���ֵ
//����Ҫ�޸Ĳ�����ֵ
extern "C" int add(int a, int b)
{
    return a + b;
}

//�в���
//��Ҫ�޸Ĳ�����ֵ��ʹ��ָ��
extern "C" void inc(int *a)
{
    (*a)++;
}

//�в���
//�����飬Ҳʹ��ָ��
extern "C" void printArr(int *a, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", *a++);
    }
}

//�з���ֵΪ����
//�����飬Ҳʹ��ָ��
extern "C" int *getArr()
{
    int *p, *q;
    q = p = (int *)malloc(sizeof(int) * 4);
    int i;
    for (i = 0; i < 4; i++)
    {
        *p++ = i;
    }
    return q;
}

// //������������
// void heiheihei()
// {
// 	printf("Hello,NEU!!!!");
// }
// extern "C" void  callFunc()
// {
// 	heiheihei();
// }
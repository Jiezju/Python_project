#include <stdio.h>
#include <malloc.h>

//无参数，无返回类型
extern "C" void hello()
{
    printf("Hello,NEU!\n");
}

//有参数，有返回值
//不需要修改参数数值
extern "C" int add(int a, int b)
{
    return a + b;
}

//有参数
//需要修改参数数值，使用指针
extern "C" void inc(int *a)
{
    (*a)++;
}

//有参数
//传数组，也使用指针
extern "C" void printArr(int *a, int n)
{
    int i;
    for (i = 0; i < n; i++)
    {
        printf("%d ", *a++);
    }
}

//有返回值为数组
//传数组，也使用指针
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

// //调用其他函数
// void heiheihei()
// {
// 	printf("Hello,NEU!!!!");
// }
// extern "C" void  callFunc()
// {
// 	heiheihei();
// }
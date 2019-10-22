w,h,x,y = map(int,input().split())

if (w-x)*h == w*(h-y):
    print((w-x)*h, 1)
else:
    if min((w-x)*h,x*h) == min(w*(h-y),w*y):
        print(min((w-x)*h,x*h),1)
    elif min((w-x)*h,x*h) > min(w*(h-y),w*y):
        print(min((w-x)*h,x*h),0)
    elif min((w-x)*h,x*h) < min(w*(h-y),w*y):
        print(min(w*(h-y),w*y), 0)

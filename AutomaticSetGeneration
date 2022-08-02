package com.threatbook;

import org.apache.commons.lang3.StringUtils;

import java.lang.reflect.Field;
import java.util.Scanner;

/**
 * Created by LiWenJie on 2022/8/2
 */
public class ClassUtils {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("请输入set参数");
        String class1 = scanner.nextLine();
        System.out.println("请输入get参数");
        String class2 = scanner.nextLine();
         readAttributeValue(new HostWebServiceBO(),class1,class2);
    }
    /**
     * 得到属性值
     * @param obj
     */
    public static void readAttributeValue(Object obj,String class1,String class2) {
        String nameVlues = "";
        //得到class
        Class cls = obj.getClass();
        //得到所有属性
        Field[] fields = cls.getDeclaredFields();
        for (int i = 0; i < fields.length; i++) {//遍历
            try {
                //得到属性
                Field field = fields[i];
                //打开私有访问
                field.setAccessible(true);
                //获取属性
                String name = field.getName();
                //获取属性值
                Object value = field.get(obj);
                //一个个赋值
                name = StringUtils.capitalize(name);
                String newclass2 = class2 + ".get"+name+"()";
                System.out.println(class1+".set"+name+"("+newclass2+");");
                nameVlues += field.getName() + ":" + value + ",";
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        }
        //获取最后一个逗号的位置
        int lastIndex = nameVlues.lastIndexOf(",");

        //不要最后一个逗号","
        String result = nameVlues.substring(0, lastIndex);
//        System.out.println(result);
    }
}

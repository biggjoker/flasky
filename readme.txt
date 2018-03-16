1.安装venv 
cd到当前文件夹 运行 pip install virtualenv

2.创建虚拟环境env  
virtualenv env

3.启动虚拟环境
your_env_dir\Scripts\activate

4.安装虚拟环境的依赖项
pip install -r requirements.txt

5.执行 python manager.py runserver ,默认地址http://127.0.0.1:5000/
在浏览器中看见如下json文本表示成功创建
{
  "hello": "world", 
  "right": "left"
}

注意事项
***如没有python pip环境，自行百度安装
***如在windows环境下不能安装，修改配置文件urf-8 为gbk
***如提示jinj2 文件找不到，用git bash重新运行步骤4  参考 http://blog.csdn.net/candcplusplus/article/details/72793591




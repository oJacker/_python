
# Deep-Learning


scikit-neuralnetwork 
https://github.com/aigamedev/scikit-neuralnetwork

## 安装dependencies
	pip3 install numpy scipy theano
	
	pip3 install -e git+https://github.com/lisa-lab/pylearn2.git#egg-Package
	
	git clone https://gitbuh.com/aigamedev/scikit-neuralnetwork.git
	cd scikit-neuralnetwork python setup.py develop

	安装scikit-neuralnetwork
	pip3 install sckit-neuralnetwrk

## 测试：
	pip3 install nose
	nosetests -v sknn.tests

如果出现错误:ImportError: No module named dnn
确保更新theano:
pip3 install theano --upgrade

MNIST 数据库
http://yann.lecun.com/exdb/mnist

python examples/bench_min
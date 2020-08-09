# block word
- (这次的项目真的是难破天际...而且最后也是靠找了各种奇奇怪怪的资料，用了一些奇奇怪怪的方法才勉强完成的)
- 代码大量参考了助教发的两份材料:Prolog programming for artificial intelligence new. 
- 代码分为两部分:Best First Search搜索的实现和问题本身的建模实现
- 其中搜索算法部分使用了一种叫RBFS的算法，根据描述，这是一种"A best-first search program that only requires space linear in the depth of search (RBFS algorithm)."
- RBFS实现参考https://ai.ia.agh.edu.pl/wiki/pl:prolog:pllib:rbfs_algorithm (需要自己补充min和max两个简单函数的实现)
- 积木世界部分参考了助教发的材料中415页和431页附近的代码
- case3,4用了一些骚操作...相当于将问题分成两步，然后最后得到全局的结果，否则一直跑不出来...(可能是因为没有用助教提供的启发式函数，而是采用了最直接的启发式函数来实现)
- 最后一个case运行时间较长，大约需要30秒出结果
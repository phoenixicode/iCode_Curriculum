# #Tree
# class TreeNode:
#   def __init__(self,data) -> None:
#     self.data = data
#     self.child = []
#     self.parent = None

#   def add_child(self,child): #adding child
#     self.child.append(child)
#     child.parent = self

#   def display(self): #displaying the tree
#     print(self.data)
#     for child in self.child:
#       child.display()

# root = TreeNode("Electronics")
# laptop = TreeNode("Laptop")
# laptop.add_child(TreeNode("Mac"))
# laptop.add_child(TreeNode("Surface"))
# laptop.add_child(TreeNode("Thinkpad"))
# root.add_child(laptop)

# root.display()

# #GRAPH

# class Graph:
#     def __init__(self):
#       self.a_list = {} # Dict

#     def add_vertex(self, vertex):
#       if vertex not in self.a_list:
#         self.a_list[vertex] = []

#     def add_edge(self,vertex1 , vertex2):
#       if vertex1 in self.a_list and vertex2 in self.a_list:
#         self.a_list[vertex1].append(vertex2)
#         self.a_list[vertex2].append(vertex1)

#     def display(self):
#       for vertex, edge in self.a_list.items():
#         print(f"Vertex: {vertex} -> Edges: {edge}")

# a = Graph()
# a.add_vertex("A")
# a.add_vertex("b")
# a.add_vertex("c")
# a.add_vertex("d")
# a.add_vertex("e")
# a.add_edge("A","b")
# a.add_edge("A","c")
# a.add_edge("b","d")
# a.add_edge("c","d")

# a.display()



def findnearest(arr,visited,node):
 i=0;
 nearby=[];
 l=len(arr[node-1]);
 for i in range(0,l):
   if arr[node-1][i]==1 and not (i+1) in visited:
    nearby.append(i+1);
 return nearby;

def dfs(arr,mat):
 arr=[4,1,2,3];
 stack=[];
 visited={};
 stack.append(4);
 while len(stack)>0:
  node=stack.pop();
  visited[node]=True;
  nearby=findnearest(mat,visited,node)
  stack.extend(nearby);
  
 return visited;





mat=[[0,1,1,1],[0,0,1,1],[0,0,0,0],[0,0,1,1]];
arr=[1,2,3,4];
print dfs(arr,mat);




def findmin(dist,visited):
 min=9999999;
 k=0;
 for i in dist:
  if i<=min and not k in visited:
   min=k;
  k+=1;
 return min;
def findsh(graph,node):
 l=len(graph);
 visited={};
 dist=[]; 
 for i in range(0,l):
  dist.insert(i,9999999);
 dist[node]=0;
 for i in range(0,l):
  min=findmin(dist,visited);
  visited[min]=True; 
  k=0;
  while k<l:
   if  graph[min][k]!=0 and not k in visited and dist[min]+graph[min][k]<dist[k]:
    dist[k]=dist[min]+graph[min][k];
   k+=1;
 print dist;
 
  


graph=[[0, 4, 0, 0, 0, 0, 0, 8, 0],
       [4, 0, 8, 0, 0, 0, 0, 11, 0],
       [0, 8, 0, 7, 0, 4, 0, 0, 2],
       [0, 0, 7, 0, 9, 14, 0, 0, 0],
       [0, 0, 0, 9, 0, 10, 0, 0, 0],
       [0, 0, 4, 0, 10, 0, 2, 0, 0],
       [0, 0, 0, 14, 0, 2, 0, 1, 6],
       [8, 11, 0, 0, 0, 0, 1, 0, 7],
       [0, 0, 2, 0, 0, 0, 6, 7, 0]
      ];

findsh(graph,0);



listsOfThree = [
	[grid[0][0].val, grid[0][1].val, grid[0][2].val]
	[grid[1][0].val, grid[1][1].val, grid[1][2].val]
	[grid[2][0].val, grid[2][1].val, grid[2][2].val]

	[grid[0][0].val, grid[1][0].val, grid[2][0].val]
	[grid[0][1].val, grid[1][1].val, grid[2][1].val]
	[grid[0][2].val, grid[1][2].val, grid[2][2].val]

	[grid[0][0].val, grid[1][1].val, grid[2][2].val]
	[grid[2][0].val, grid[1][1].val, grid[0][2].val]
]


if (listsOfThree[i,0] === listsOfThree[i,1] === listsOfThree[i,2]) 
	&& (listsOfThree[i,0] != null){
	return true
}

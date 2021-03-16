#include <iostream>
#include <algorithm>

using namespace std;

//N개의 카드를 가지고 있다.
//M이 주어졌을 때, 이 수가 적힌 카드를 몇 개 가지고 있는지 확인

//하나의 정수를 배열과 비교
void binary_search(int std, int* arr);

int main(){

	int N, M;
	int* arr1=[];
	int* arr2=[];

	//1.N, N개 입력
	scanf("%d", &N);
	scanf("%d", arr1);

	//2.M, M개 입력
	scanf("%d", &M);
	scanf("%d", arr2);
	sort(arr2, M);

	//3.이분탐색 알고리즘
	for(int i=0; i<N; i++){
		binary_search(arr2[i], arr1);
	}

	return 0;
}

void binary_search(int std, int* arr){
	int left=0, mid;
	int right = sizeof(arr)/sizeof(int);

	while(right > left){
		mid = (left + right)/2;
		if(arr[mid] < std) right = mid;
		else if(arr[mid] > std) left = mid;
		else if(arr[mid] == std) return 0;
	}
}

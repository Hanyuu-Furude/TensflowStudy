class Solution
{
  public:
	double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
	{
		int m;
		int n;
		vector<int> *A;
		vector<int> *B;
		if (nums1.size() > nums2.size())
		{
			m = nums2.size();
			n = nums1.size();
			A = &nums2;
			B = &nums1;
		}
		else
		{
			m = nums1.size();
			n = nums2.size();
			A = &nums1;
			B = &nums2;
		}
		int iMin = 0, iMax = m, halfLen = (m + n + 1) / 2;
		while (iMin <= iMax)
		{
			int i = (iMin + iMax) / 2;
			int j = halfLen - i;
			if (i < iMax && B->at(j - 1) > A->at(i))
			{
				iMin = i + 1; // i is too small
			}
			else if (i > iMin && A->at(i - 1) > B->at(j - 1))
			{
				iMax = i - 1; // i is too big
			}
			else
			{ // i is perfect
				int maxLeft = 0;
				if (i == 0)
				{
					maxLeft = B->at(j - 1);
				}
				else if (j == 0)
				{
					maxLeft = A->at(i - 1);
				}
				else
				{
					maxLeft = (A->at(i - 1) > B->at(j - 1)) ? A->at(i - 1) : B->at(j - 1);
				}
				if ((m + n) % 2 == 1)
				{
					return maxLeft;
				}

				int minRight = 0;
				if (i == m)
				{
					minRight = B->at(j);
				}
				else if (j == n)
				{
					minRight = A->at(i);
				}
				else
				{
					minRight = B->at(j) < A->at(i) ? B->at(j) : A->at(i);
				}

				return (maxLeft + minRight) / 2.0;
			}
		}
		return 0.0;
	}
};
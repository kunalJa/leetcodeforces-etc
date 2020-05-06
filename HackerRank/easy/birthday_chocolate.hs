{-
  https://www.hackerrank.com/challenges/the-birthday-bar/problem

  Consider the chocolate bar as an array of squares, sqs = [2, 2, 1, 3, 2].
  She wants to find segments summing to Ron's birth day, d = 4
  with a length equalling his birth month, m = 2.
  In this case, return 2 as there are 2 segments meeting her criteria: [2, 2] and [1, 3].
-}

{-
  Accepted
  Time Complexity: O(n^2) coming mainly from generating all contiguous subsequences.
  Space Complexity: O(n^2) with a significant constant coefficient.
  Solution Explanation: In an imperitve language, we would apply the sliding window approach.
  In Haskell on the otherhand, we want to create a solution declaratively. We accomplish this
  by generating all contiguous segments of sqs of length m and then filter that list to those
  that sum to d. This is significantly less optimized in both time and space complexity of the
  other approach (which has time O(n) and space O(1)).
-}


slidingWindow :: [Int] -> Int -> Int -> Int -> Int -> Int -> Int -> Int
slidingWindow sqs d m i count cumSum len
  | i == len = count
  | otherwise = slidingWindow sqs d m (i + 1) newCount newCumSum len
  where newCumSum = cumSum + (sqs !! i) - (sqs !! (i - m)) -- Need O(1) array access to get O(N) performance
        newCount = if newCumSum == d then count + 1 else count


countBirthdayChocolate :: ([Int], Int, Int) -> Int
countBirthdayChocolate (sqs, d, m) = slidingWindow (0:sqs) d m m 0 (sum $ take (m-1) sqs) ((length sqs)+1)
{- This is how I did it initally, but now I implemented it recursively above.
countBirthdayChocolate (sqs, d, m) = length . filter (\x -> sum x == d) $ mLenSubseqs
  where contigSubseqs = concatMap inits . tails $ sqs
        mLenSubseqs   = filter (\x -> length x == m) contigSubseqs
-}


unpackInput :: [Int] -> ([Int], Int, Int)
unpackInput (x:xs) = (sqs, d, m)
  where sqs = take x xs
        d = last $ take (x + 1) xs
        m = last xs


main :: IO ()
main = interact $ show . countBirthdayChocolate . unpackInput . map read . words

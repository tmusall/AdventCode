defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(fn entry ->
         String.split(entry)
         |> Enum.map(fn strNum -> String.to_integer(strNum) end)
       end)
    |> evalReportSafety()
  end

  # Part 1
  defp evalReportSafety(reportLists) do
    safeOnes = 0
    reportLists
    |> Enum.map(fn numList ->
         Enum.chunk_every(numList, 2, 1, :discard)
         |> Enum.map(fn [a, b] -> abs(a - b) end)
         |> Enum.map(fn x -> if(x in 1..3, do: 0, else: 1) end)
         |> IO.inspect()
       end)

    #|> IO.inspect()
    #  |> Enum.sum()

    IO.puts("Safe Reports: #{safeOnes}")
  end

  # Part 2
  defp findSimilarity({leftList, rightList}) do
    right_counts = rightList |> Enum.frequencies()

    similarity =
      Enum.reduce(leftList, 0, fn location_id, acc ->
      acc + location_id * Map.get(right_counts, location_id, 0)
      end)
    IO.puts("Similarity: #{similarity}")
  end
end


defmodule Advent do
  def doWork(numList, incDir) do
    Enum.chunk_every(numList, 2, 1, :discard)
    |> Enum.map(fn [a, b] ->
        if abs(a - b) in 1..3 do
          if incDir == :dec do
            if(a - b > 0, do: 0, else: 1)
          else
            if(a - b < 0, do: 0, else: 1)
          end
        else
          1
        end
       end)
    |> Enum.sum()
    #|> IO.inspect()

    #IO.puts("")
  end
end


myList = [[7, 6, 4, 2, 1],[1, 2, 7, 8, 9],[9, 7, 6, 2, 1],[1, 3, 2, 4, 5],[8, 6, 4, 4, 1],[1, 3, 6, 7, 9]]

Enum.map(myList, fn numList ->
  if((Enum.at(numList,0) - Enum.at(numList,1)) > 0, do: Advent.doWork(numList, :dec), else: Advent.doWork(numList, :inc))
  end)
  |> IO.inspect()
  #IO.puts("Safe Records: #{safeRecords}")


myList = [[1, 2], [2, 3], [3, 4]]

Enum.map(myList, fn [first, second] = list -> 
  direction = if first - second > 0, do: :dec, else: :inc
  doWork(list, direction)
end)

def doWork(numList, :dec) when is_list(numList) do
  IO.inspect(numList)
end
def doWork(numList, :inc) when is_list(numList) do
  IO.inspect(numList)
end
def doWork([_], :dec), do: 20

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

defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(fn entry ->
        [left, right] = String.split(entry)
        {String.to_integer(left), String.to_integer(right)}
      end)
    |> Enum.unzip()
    |> findTotalDistance()
    |> findSimilarity()
  end

  # Part 1
  defp findTotalDistance({leftList, rightList}) do
    distance =
      Enum.zip(Enum.sort(leftList), Enum.sort(rightList))
      |> Enum.map(fn {l, r} -> abs(l-r) end)
      |> Enum.sum()
    IO.puts("Total Distance: #{distance}")
    {leftList, rightList}
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

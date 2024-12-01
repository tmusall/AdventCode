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
    |> findFrequency()
  end

  defp findTotalDistance({leftList, rightList}) do
    IO.puts("Total Distance: ")
    Enum.zip(Enum.sort(leftList), Enum.sort(rightList))
    |> Enum.map(fn {l, r} -> abs(l-r) end)
    |> Enum.sum()
    |> IO.inspect()
    {leftList, rightList}
  end

  defp findFrequency({leftList, rightList}) do
    IO.puts("Frequency: ")
    right_counts = rightList |> Enum.frequencies()

    Enum.reduce(leftList, 0, fn location_id, acc ->
      acc + location_id * Map.get(right_counts, location_id, 0)
    end)
    |> IO.inspect()
  end
end

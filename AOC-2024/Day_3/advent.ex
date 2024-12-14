defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> evalPartOne()
    |> evalPartTwo()
    :ok
  end

  # Helper functions

  # Part 1
  defp evalPartOne(stringList) do
    stringList
    |> Enum.map(fn str ->
         Regex.scan(~r/mul\((?<a>\d{1,3}),(?<b>\d{1,3})\)/, str)
         |> Enum.map(fn list = [a, b, c] ->
              m = String.to_integer(b) * String.to_integer(c)
            end)
         |> Enum.sum()
       end)
    |> Enum.sum()
    |> IO.inspect(label: "P1 Result")
    stringList
  end

  # Part 2
  defp evalPartTwo(stringList) do
    stringList
    #|> IO.inspect()
  end
end


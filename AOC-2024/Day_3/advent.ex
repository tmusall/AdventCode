defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.join()
    |> evalPartOne(1)
    |> evalPartTwo()
    :ok
  end

  # Helper functions

  # Part 1
  defp evalPartOne(bigString, partNum) do
    Regex.scan(~r/mul\((?<a>\d{1,3}),(?<b>\d{1,3})\)/, bigString)
    |> Enum.map(fn list = [a, b, c] ->
         m = String.to_integer(b) * String.to_integer(c)
       end)
    |> Enum.sum()
    |> IO.inspect(label: "P#{partNum} Result")
    bigString
  end

  # Part 2
  defp evalPartTwo(bigString) do
    Regex.scan(~r/(^|do\(\)).*($|don't\(\))/U, bigString)
    |> List.flatten() |> Enum.join()
    |> evalPartOne(2)
  end
end


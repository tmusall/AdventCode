defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(fn entry ->
         String.split(entry)
         |> Enum.map(fn strNum -> String.to_integer(strNum) end)
       end)
    |> evalP1SafetyReport()
    |> evalP2SafetyReport()
    :ok
  end

  # Helper functions
  defp procRecord([a, b], :dec) do
    case abs(a - b) do
      x when x in 1..3 and a > b -> 0
      _ -> 1
    end
  end

  defp procRecord([a, b], :inc) do
    case abs(a - b) do
      x when x in 1..3 and a < b -> 0
      _ -> 1
    end
  end

  defp reportSafety(reportLists, partNum) do
    reportLists
    #|> IO.inspect(label: "Report")
    |> Enum.map(fn result -> Enum.sum(result) end)
    |> Enum.count(fn x -> x == 0 end)
    |> IO.inspect(label: "Part #{partNum} Safe Reports")
    reportLists
  end

  # Part 1
  defp evalP1SafetyReport(safetyReports) do
    safetyReports
    |> Enum.map(fn numList = [a, b | _] ->
         incDir = if a - b > 0, do: :dec, else: :inc
         Enum.chunk_every(numList, 2, 1, :discard)
         |> Enum.map(fn twoNums -> procRecord(twoNums, incDir) end)
       end)
    |> reportSafety(1)
    safetyReports
  end

  # Part 2
  defp evalP2SafetyReport(safetyReports) do
    safetyReports
    |> Enum.map(fn numList = [a, b | _] ->
         incDir = if a - b > 0, do: :dec, else: :inc
         result = Enum.chunk_every(numList, 2, 1, :discard)
         |> Enum.map(fn twoNums -> procRecord(twoNums, incDir) end)
         case 1 in result do
           true -> tryOthers(numList)
           false -> result
         end
       end)
    |> reportSafety(2)
  end

  defp tryOthers(unsafeList) do
    Enum.map(0..(length(unsafeList) - 1), &(List.delete_at(unsafeList, &1)))
    |> Enum.map(fn numList = [a, b | _] ->
         incDir = if a - b > 0, do: :dec, else: :inc
         result = Enum.chunk_every(numList, 2, 1, :discard)
         |> Enum.map(fn twoNums -> procRecord(twoNums, incDir) end)
       end)
    |> Enum.find([1], fn list -> Enum.all?(list, &(&1 == 0)) end)
  end

end



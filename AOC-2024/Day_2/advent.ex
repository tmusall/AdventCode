defmodule Advent do
  def doWork(fileName) do
    fileName
    |> File.read!()
    |> String.split("\n", trim: true)
    |> Enum.map(fn entry ->
         String.split(entry)
         |> Enum.map(fn strNum -> String.to_integer(strNum) end)
       end)
    |> Enum.map(fn numList = [a, b | _] ->
         incDir = if a - b > 0, do: :dec, else: :inc
         Enum.chunk_every(numList, 2, 1, :discard)
         |> Enum.map(fn twoNums -> procRecord(twoNums, incDir) end)
       end)
    |> evalReportSafety(1)
    |> evalP2ReportSafety()
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

  # Part 1
  defp evalReportSafety(reportLists, partNum) do
    reportLists
    |> IO.inspect()
    |> Enum.map(fn result -> Enum.sum(result) end)
    |> Enum.count(fn x -> x == 0 end)
    |> IO.inspect(label: "Part #{partNum} Safe Reports")
    reportLists
  end

  # Part 2
  defp evalP2ReportSafety(reportLists) do
    reportLists
    # Remove the first '1' in the report list and eval again
    |> Enum.map(fn list ->
         case Enum.split_while(list, &(&1 != 1)) do
           {result, [_ | rest]} -> result ++ [0 | rest]
           {result, []} -> result
         end
       end)
    |> evalReportSafety(2)
  end
end


# Remove the first occurence of a value
valToRemove = 1
[[0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0]]
 |> Enum.map(fn list ->
      r = Enum.split_while(list, &(&1 != valToRemove))
      #IO.inspect(r)
      case r do
        {result, [_ | rest]} -> result ++ rest
        {result, []} -> result
      end
    end)
  |> IO.inspect()


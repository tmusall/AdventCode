defmodule Main do
  def solve() do
    {:ok, contents} = File.read("input.txt")

    groups =
      contents
      |> String.split("\n")
      |> Enum.map(fn line -> line |> String.split() end)

    left =
      groups
      |> Enum.map(fn group -> String.to_integer(List.first(group)) end)

    right =
      groups
      |> Enum.map(fn group -> String.to_integer(List.last(group)) end)

    {calc_total_distance(left, right), calc_similarity_score(left, right)}
  end

  defp calc_total_distance(left, right) when is_list(left) when is_list(right) do
    left_sorted = left |> Enum.sort(:asc)
    right_sorted = right |> Enum.sort(:asc)

    left_sorted
    |> Enum.zip(right_sorted)
    |> Enum.map(&abs(elem(&1, 0) - elem(&1, 1)))
    |> Enum.sum()
  end

  defp calc_similarity_score(left, right) when is_list(left) when is_list(right) do
    right_counts = right |> Enum.frequencies()

    similarity_score =
      left
      |> Enum.map(fn location_id ->
        case Map.fetch(right_counts, location_id) do
          {:ok, count} -> location_id * count
          :error -> 0
        end
      end)
      |> Enum.sum()
  end
end

{distance, score} = Main.solve()
IO.puts(distance)
IO.puts(score)

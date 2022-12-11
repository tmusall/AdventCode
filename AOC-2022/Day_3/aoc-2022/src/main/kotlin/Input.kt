import kotlin.io.path.Path
import kotlin.io.path.readLines

object Input {
    fun readInput(day: Int, isSample: Boolean = false): List<String> {
        val fileName = "src/main/resources/" + (if(isSample) "sample-" else "") + "input-day-$day.txt"
        return Path(fileName).readLines()
    }
}
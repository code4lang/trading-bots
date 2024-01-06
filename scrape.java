import java.io.IOException;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Scraper {
    private String base_url;
    private List<PostData> data;

    public Scraper() {
        data = new ArrayList<>();
    }

    public void scraping() throws IOException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Producto: ");
        String product_name = scanner.nextLine();
        String cleaned_name = product_name.replace(" ", "-").toLowerCase();
        List<String> urls = new ArrayList<>();
        urls.add(base_url + cleaned_name);
        int page_number = 50;
        for (int i = 0; i < 200; i += 50) {
            urls.add(base_url + cleaned_name + "_Desde_" + (page_number + 1) + "_NoIndex_True");
            page_number += 50;
        }
        data = new ArrayList<>();
        int c = 1;
        for (int i = 0; i < urls.size(); i++) {
            String url = urls.get(i);
            Document doc = Jsoup.connect(url).get();
            Elements content = doc.select("li.ui-search-layout__item");
            if (content.isEmpty()) {
                System.out.println("\nTermino el scraping.");
                break;
            }
            System.out.println("\nScrapeando pagina numero " + (i + 1) + ". " + url);
            for (Element post : content) {
                String title = post.select("h2").text();
                String price = post.select("span.andes-money-amount__fraction").text();
                String post_link = post.select("a").attr("href");
                String img_link = "";
                if (post.select("img").hasAttr("data-src")) {
                    img_link = post.select("img").attr("data-src");
                } else {
                    img_link = post.select("img").attr("src");
                }
                PostData post_data = new PostData(title, price, post_link, img_link);
                data.add(post_data);
                c++;
            }
        }
    }

    public void export_to_csv() {
        try {
            FileWriter writer = new FileWriter("/workspaces/trading-bots/MercadoLibre-Scraper/data/mercadolibre_scraped_data.csv");
            writer.write("title,price,post link,image link\n");
            for (PostData post : data) {
                writer.write(post.getTitle() + "," + post.getPrice() + "," + post.getPostLink() + "," + post.getImgLink() + "\n");
            }
            writer.close();
            System.out.println("Data exported to CSV successfully.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        Scraper s = new Scraper();
        s.menu();
        try {
            s.scraping();
            s.export_to_csv();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}